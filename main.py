#
# This file is part of Brazil Data Cube Landsat Angles Docker.
# Copyright (C) 2022 INPE.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.
#

import os
import sys
from pathlib import Path

if len(sys.argv) < 2:
    print('missing args, use SCENEID')
    sys.exit()

#
# Defining the working directory
#
work_dir = Path(f'/work/{sys.argv[1]}')
work_dir.mkdir(parents=True, exist_ok=True)
os.chdir(work_dir)

#
# Generating bands
#
os.system(f'/app/l8_angles/l8_angles /mnt/input-dir/{sys.argv[1]}/{sys.argv[1]}_ANG.txt BOTH 1 -b 4')

#
# Creating the output directory
#
output_directory = f"/mnt/output-dir/{sys.argv[1]}"
os.makedirs(output_directory, exist_ok=True)

#
# Exporting each band
#
os.system(f'gdal_translate -co "COMPRESS=DEFLATE" -b 1 {work_dir}/{sys.argv[1]}_sensor_B04.img {output_directory}/{sys.argv[1]}_VAA.tif')
os.system(f'gdal_translate -co "COMPRESS=DEFLATE" -b 2 {work_dir}/{sys.argv[1]}_sensor_B04.img {output_directory}/{sys.argv[1]}_VZA.tif')
os.system(f'gdal_translate -co "COMPRESS=DEFLATE" -b 1 {work_dir}/{sys.argv[1]}_solar_B04.img {output_directory}/{sys.argv[1]}_SAA.tif')
os.system(f'gdal_translate -co "COMPRESS=DEFLATE" -b 2 {work_dir}/{sys.argv[1]}_solar_B04.img {output_directory}/{sys.argv[1]}_SZA.tif')
