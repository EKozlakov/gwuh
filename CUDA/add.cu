//written by Dr. Dov Kruger

#include <stdio.h>

__global__
void saxpy(int n, float a, const float *x, float *y)
{
  int i = blockIdx.x*blockDim.x + threadIdx.x;
  if (i < n) y[i] = a*x[i] + y[i];
}

int main() {
  int N = 1<<20; // 1024*1024 = 1M
  float *x, *y, *d_x, *d_y;
  x = (float*)malloc(N*sizeof(float)); // allocate memory on CPU
  y = (float*)malloc(N*sizeof(float));
  for (int i = 0; i < N; i++) {
    x[i] = 1.0f;
    y[i] = 2.0f;
  }

  cudaMalloc(&d_x, N*sizeof(float));  // d_x = new allocated memory on GPU
  cudaMalloc(&d_y, N*sizeof(float));
  cudaMemcpy(d_x, x, N*sizeof(float), cudaMemcpyHostToDevice); //copy to GPU
  cudaMemcpy(d_y, y, N*sizeof(float), cudaMemcpyHostToDevice);

  // Perform SAXPY on 1M elements
  saxpy<<<(N+255)/256, 256>>>(N, 2.0f, d_x, d_y);

  cudaMemcpy(y, d_y, N*sizeof(float), cudaMemcpyDeviceToHost); // copy back to CPU

  float maxError = 0.0f;
  for (int i = 0; i < N; i++)
    maxError = max(maxError, abs(y[i]-4.0f));
  printf("Max error: %f\n", maxError);

  cudaFree(d_x); // free the memory on the GPU
  cudaFree(d_y);
  free(x);  // free the memory on the CPU
  free(y);
}