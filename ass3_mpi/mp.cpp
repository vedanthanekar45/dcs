#include <iostream>
#include <vector>
#include <numeric>
#include <mpi.h>
using namespace std;

int main (int argc, char** argv) {
    MPI_Init(&argc, &argv);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    const int array_size = 1000;
    vector<int> data;
    int elements_per_proc = array_size/world_size;
    vector<int> local_array(elements_per_proc);

    if (world_rank == 0) {

        if (array_size % world_size != 0) {
            std::cerr << "Total elements N must be divisible by the number of processors." << endl;
            MPI_Abort(MPI_COMM_WORLD, 1);
        }

        cout << "Total elements (N): " << array_size << std::endl;
        cout << "Number of processors (n): " << world_size << std::endl;
        cout << "Elements per processor (N/n): " << elements_per_proc << std::endl;
        cout << "------------------------------------------" << std::endl;

        data.resize(array_size);
        iota(data.begin(), data.end(), 1);
    }

    MPI_Scatter(
        data.data(),
        elements_per_proc,
        MPI_INT,
        local_array.data(),
        elements_per_proc,
        MPI_INT,
        0,
        MPI_COMM_WORLD
    );

    long long local_sum = 0;
    for (int i = 0; i < elements_per_proc; i++) {
        local_sum += local_array[i];
    }
    cout << "Process " << world_rank << " Calculated Intermediate Sum: " << local_sum << endl;

    vector<long long> intermediate_sums;
    if (world_rank == 0) {
        intermediate_sums.resize(world_size);
    }

    MPI_Gather(
        &local_sum,
        1,
        MPI_LONG_LONG,
        world_rank == 0 ? intermediate_sums.data() : nullptr,
        1,
        MPI_LONG_LONG,
        0,
        MPI_COMM_WORLD
    );

    if (world_rank == 0) {
        long long total_sum = 0;
        for (long long sum : intermediate_sums) {
            total_sum += sum;
        }
        cout << "------------------------------------------" << endl;
        cout << "Final total sum calculated at root: " << total_sum << endl;
    }

    MPI_Finalize();
    return 0;
}