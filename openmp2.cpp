#include <stdio.h>
#include <omp.h>

int main(int argc, char** argv){
     int total_Sum = 0;
     int partial_Sum;
    #pragma omp parallel private(partial_Sum) shared(total_Sum)
    {
        #pragma omp single
        {
          printf("Number of threads: %d\n", omp_get_num_threads());
        }
        
        partial_Sum = 0;
        #pragma omp for
        for(int i = 1; i <= 1000; i++){
            partial_Sum += i;
        }

        //Create thread safe region.
        #pragma omp critical
        { // implemented with mutex
                //add each threads partial sum to the total sum
                total_Sum += partial_Sum;
        }
    }
    
    printf("Total Sum: %d\n", total_Sum);
    return 0;
}