from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from firebase_admin import db
from datetime import datetime


class LandingAPI(APIView):
    """
    Vista API para operaciones CRUD en Firebase Realtime Database
    """
    name = "Landing API"
    collection_name = "landing"  # Nombre de la colección en Firebase
    
    def get(self, request):
        """
        GET: Obtener todos los elementos de la colección
        """
        # Referencia a la colección
        ref = db.reference(f'{self.collection_name}')
        
        # get: Obtiene todos los elementos de la colección
        data = ref.get()
        
        # Devuelve un arreglo JSON
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        """
        POST: Crear un nuevo registro en la colección
        """
        data = request.data
        
        # Referencia a la colección
        ref = db.reference(f'{self.collection_name}')
        
        # Obtener fecha y hora actual con formato personalizado
        current_time = datetime.now()
        custom_format = current_time.strftime("%d/%m/%Y, %I:%M:%S %p").lower().replace('am', 'a. m.').replace('pm', 'p. m.')
        data.update({"timestamp": custom_format})
        
        # push: Guarda el objeto en la colección
        new_resource = ref.push(data)
        
        # Devuelve el id del objeto guardado
        return Response({"id": new_resource.key}, status=status.HTTP_201_CREATED)