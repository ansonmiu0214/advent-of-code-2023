FROM silkeh/clang:17

RUN apt-get update                                                             \
    && apt-get install -y build-essential cmake gdb software-properties-common \
    && apt-get clean

# Tell CMake to use the Clang compiler.

ENV CC=/usr/bin/clang
ENV CXX=/usr/bin/clang++

RUN mkdir /buildarea

WORKDIR /workarea
