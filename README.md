# Landsat-angles-docker

Landsat Angles Creation Tools

## Dependencies

- Docker

## Installation

1. Download or clone this repository;

2. Run

   ```bash
   $ docker build -t brazildataube/landsat-angles .
   ```

   from the root of this repository.

## Usage

To process a Landsat-8 scene (e.g. `LC08_L2SP_222081_20190502_20200829_02_T1`) run

```bash
$ docker run --rm \
    -v /path/to/input/:/mnt/input-dir:rw brazildataube/landsat-angles LC08_L2SP_222081_20190502_20200829_02_T1
```

Results are written on input-dir

## Acknowledgements

Landsat Ang Tool is developed and a property of USGS, more info can be found at https://www.usgs.gov/core-science-systems/nli/landsat/solar-illumination-and-sensor-viewing-angle-coefficient-files?qt-science_support_page_related_con=1#qt-science_support_page_related_con
