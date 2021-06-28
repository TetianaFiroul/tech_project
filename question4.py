"""
    addition
"""
import random



from peer import Peer
from simulation import Simulation, BINS
from histogram import compute_histogram_bins, plot_histogram


class PeerQ4(Peer):

    def send_data_to_backend(self):
        """
            Question 4: to optimised processing time and resource 
            we can use random sampling. 
            The samle size should be greater than 30% in order to generate properly the backend_database
            The distribution law stays the same. 
        """
        connection_duration=list(self.peer_pool.values())
        sample_rate = 0.3
        sample_size = int(len(connection_duration)*sample_rate)
        connection_duration=random.sample(connection_duration, sample_size)
        return connection_duration

class SimulationQ4(Simulation):

    def generate_network(self):
        self.network = [PeerQ4() for _ in range(self.number_of_peers)]

    def process_backend_data(self):
        """
            Question 4: to optimised processing time and resource 
            we can use random sampling. 
            The distribution law stays the same even with a sample size 10%
        """
        sample_rate = 0.1
        connection_duration=[i for j in self.backend_database for i in j]
        final_data = random.sample(connection_duration, int(0.1*self.number_of_peers))
        histogram_bins=compute_histogram_bins(final_data,BINS)
        #plot_histogram(histogram_bins)
        return (histogram_bins)

if __name__ == "__main__":
    
    
    s = SimulationQ4(number_of_peers=10, max_peer_pool_size=2)
    s.run()
    s.report_result()

      
    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=100)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=1000, max_peer_pool_size=1000)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=10)
    s.run()
    s.report_result()

    s = SimulationQ4(number_of_peers=10000, max_peer_pool_size=100)
    s.run()
    s.report_result()
    
    s = SimulationQ4(number_of_peers=100000, max_peer_pool_size=100)
    s.run()
    s.report_result()


