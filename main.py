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
