import os
from database import PostgresConnection
from extract_data import ExtractData
from transform_data import Guideline

class ETLMaster():

    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.parent_dir = os.path.join(self.script_dir, '..')
        self.files_to_import_path = os.path.join(self.parent_dir, "import")
        self.output_path = os.path.join(self.parent_dir, "outputs")
        self.config_path = os.path.join(self.parent_dir, "config")
        self.log_path = os.path.join(self.parent_dir, "log")
        self.connection = None
        
        os.makedirs(self.files_to_import_path, exist_ok=True)
        os.makedirs(self.output_path, exist_ok=True)
        os.makedirs(self.config_path, exist_ok=True)
        os.makedirs(self.log_path, exist_ok=True)

    def database_connection(self):        
        db = PostgresConnection(self.config_path)
        db.connect()
        return db

    def extract(self, connection):
        raw_data = ExtractData(self.files_to_import_path, connection, self.config_path)
        raw_data.read_data()
        return raw_data

    def transform(self, data):
        # Implementa la lógica para transformar los datos según tus necesidades
        processed_data = data  # En este ejemplo, la transformación es mínima
        return processed_data

    def load(self, data):
        # Implementa la lógica para cargar los datos, por ejemplo, a un archivo CSV
        data.to_csv(self.processed_data_path, index=False)

    def run_etl(self):

        self.connection = self.database_connection()

        raw_data = self.extract(self.connection)
        for data in raw_data.dfs:
            test = Guideline(data)
            test.obtain_data()
        #processed_data = self.transform(raw_data)
        #self.load(processed_data)

        self.connection.disconnect()
        print("Proceso ETL completado con éxito.")

# Uso de la clase ETLMaster
etl_master = ETLMaster()
etl_master.run_etl()