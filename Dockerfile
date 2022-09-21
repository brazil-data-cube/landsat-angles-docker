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


# osgeo/gdal
FROM osgeo/gdal@sha256:a3e05de15501b1ced05e66b6c8e5a6e5b38e20a9460393336a85fa7f5701f3a8
LABEL maintainer="Brazil Data Cube Team <brazildatacube@inpe.br>"

USER root

RUN apt-get update -y && apt-get install -y \
    make \
    gcc && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

COPY L8_ANGLES_2_7_0.tgz /app

RUN tar -xvzf /app/L8_ANGLES_2_7_0.tgz && cd /app/l8_angles && make

WORKDIR /code

COPY main.py /code

WORKDIR /work

### Run the sen2cor application
ENTRYPOINT ["python", "/code/main.py"]