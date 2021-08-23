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