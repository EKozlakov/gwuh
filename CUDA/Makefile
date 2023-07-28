CLPATH="\..\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.36.32532\bin\Hostx64\x64" #path to CUDA approved (MSVS) C++ compiler

add: add.cu
	nvcc add.cu -ccbin=$(CLPATH) -o add

displaycapabilities: displaycapabilities.cu
	nvcc displaycapabilities.cu -ccbin=$(CLPATH) -o displaycapabilities
