from minio import Minio
import os

if __name__ == "__main__":

   # Colocar o path da imagem/objeto
   FILE = "PATH"

   # Criar access key no Minio e colocar como variavel de ambiente
   ACCESS_KEY = os.getenv('ACCESS_KEY')
   SECRET_KEY = os.getenv('SECRET_KEY')

   MINIO_API_HOST = "http://localhost:9000"
   MINIO_CLIENT = Minio("localhost:9000", access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)
   found = MINIO_CLIENT.bucket_exists("baldinho")
   if not found:
      MINIO_CLIENT.make_bucket("baldinho")
   else:
      print("Bucket already exists")

   MINIO_CLIENT.fput_object("baldinho", "minhaimagem.jpeg", FILE,)
   print("It is successfully uploaded to bucket")