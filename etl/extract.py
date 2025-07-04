from typing import List
from sheets import async_get_afl, AFL_YEARS
import asyncio
from local_types.data_type import AflDataType


def extract_afl_from_sheet(year: AFL_YEARS) -> List[AflDataType]:
    afl = asyncio.run(async_get_afl(year))
    return afl
