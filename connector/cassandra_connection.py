from cassandra.cluster import Cluster

class CassandraDB:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CassandraDB, cls).__new__(cls)
            cls._instance._initialize_session()
        return cls._instance

    def _initialize_session(self):
        try:
            cluster = Cluster(['127.0.0.1'])  # Change to your Cassandra node IP
            self.session = cluster.connect('cassandrakeyspace')
            print("Connected to Cassandra successfully!")
        except Exception as e:
            print(f"Error connecting to Cassandra: {e}")
            self.session = None

    def get_session(self):
        return self.session
