# ========================================================================== #
#                                                                            #
#    KVMD - The main PiKVM daemon.                                           #
#                                                                            #
#    Copyright (C) 2018-2022  Maxim Devaev <mdevaev@gmail.com>               #
#                                                                            #
#    This program is free software: you can redistribute it and/or modify    #
#    it under the terms of the GNU General Public License as published by    #
#    the Free Software Foundation, either version 3 of the License, or       #
#    (at your option) any later version.                                     #
#                                                                            #
#    This program is distributed in the hope that it will be useful,         #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the           #
#    GNU General Public License for more details.                            #
#                                                                            #
#    You should have received a copy of the GNU General Public License       #
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.  #
#                                                                            #
# ========================================================================== #

import passlib.apache

import pytest

from . import get_configured_auth_service


# =====
@pytest.mark.asyncio
async def test_ok__radius_service(tmpdir) -> None:  # type: ignore
    async with get_configured_auth_service("radius", host="127.0.0.1", secret="testing123") as service:
        assert not (await service.authorize("user", "foo"))
        assert not (await service.authorize("admin", "foo"))
        assert not (await service.authorize("user", "pass"))
        assert (await service.authorize("admin", "pass"))
