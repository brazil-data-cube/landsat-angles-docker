..
    This file is part of Brazil Data Cube Landsat Angles Docker.
    Copyright (C) 2022 INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.



# Landsat-angles-docker

Landsat Angles Creation Tools

## Dependencies

- Docker

## Installation

1. Download or clone this repository;

2. Run

   ```bash
   $ docker build -t brazildatacube/landsat-angles .
   ```

   from the root of this repository.

## Usage

To process a Landsat-8 scene (e.g. `LC08_L2SP_222081_20190502_20200829_02_T1`) run

```bash
$ docker run --rm \
    -v /path/to/input/:/mnt/input-dir:rw brazildatacube/landsat-angles LC08_L2SP_222081_20190502_20200829_02_T1
```

Results are written on input-dir

## Acknowledgements

Landsat Ang Tool is developed and a property of USGS, more info can be found at https://www.usgs.gov/core-science-systems/nli/landsat/solar-illumination-and-sensor-viewing-angle-coefficient-files?qt-science_support_page_related_con=1#qt-science_support_page_related_con
