from django.shortcuts import render, redirect
from webApp.models import administrators, customer, payments_customer
from django.http import JsonResponse ,HttpResponse
from django.contrib.auth import logout
from django.core import serializers
import json
import jwt
from datetime import datetime, timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# Genera el token de autenticación
@api_view(['POST'])
def generate_jwt(request):
	try:
		name = request.data["user"]
		password = request.data["password"]
		if administrators.objects.filter(name=name,password=password).exists():
			obtener_rol = administrators.objects.get(name=name)		
			payload = {
				"user": request.data["user"],
				"password": request.data["password"],
				"rol":obtener_rol.rol,
				"exp": datetime.utcnow() + timedelta(days=1)
			}

			jwt_token = jwt.encode(payload, "secret_key", algorithm='HS256')
			return Response({"token": jwt_token})
		else:
			return Response({"error": "usuario o password incorrectos"})
	
	except Exception as a:
		return Response({"error":a},)

# Consulta todos los registros de la tabla customer
@api_view(['GET'])
def list_customer(request):
	rol = verify_jwt(request.headers['Apikey'])
	if rol == "administrator":
		list_objects , list_objects2 =vistas()
		return Response({"customer": list_objects})
	elif rol == "super_administrator":
		list_objects , list_objects2 =vistas()
		return Response({"customer": list_objects})

# Consulta todos los registros de la tabla payments_customer
@api_view(['GET'])
def list_payments_customer(request):
	rol = verify_jwt(request.headers['Apikey'])
	if rol == "administrator":
		list_objects , list_objects2 =vistas()
		return Response({"payments_customer": list_objects2})
	elif rol == "super_administrator":
		list_objects , list_objects2 =vistas()
		return Response({"payments_customer": list_objects2})

# Crea un registro en la tabla de customer y en payments_customer
@api_view(['POST'])
def create_customer_api(request):
	rol = verify_jwt(request.headers['Apikey'])
	if rol == "administrator":
		return Response({"error": "solo los super administrator pueden crear en customers"})
	elif rol == "super_administrator":
		data=json.loads(request.body)
		name = data['name']
		paternal_surname = data['paternal_surname']
		email = data['email']
		if customer.objects.filter(name=name, paternal_surname=paternal_surname,email=email).exists():
			data = {'mensaje': 'ya existe ese customer'}
			return JsonResponse(data)	
		else:
			nuevo_registro = customer(name=name, paternal_surname=paternal_surname,email=email)
			nuevo_registro.save()
			payments_customers = payments_customer(amount="10", customer_id=nuevo_registro,product_name="silla",quantity=2)
			payments_customers.save()

			return JsonResponse({"response": "se creo con éxito"})

# Actualiza un registro en customer
@api_view(['PUT'])
def update_customer_api(request):
	rol = verify_jwt(request.headers['Apikey'])
	if rol == "administrator":
		return Response({"error": "solo los super administrator pueden modificar en customers"})
	elif rol == "super_administrator":
		data=json.loads(request.body)
		name = data['name']
		paternal_surname = data['paternal_surname']
		email = data['email']
		id = data['pk']
		if customer.objects.filter(name=name, paternal_surname=paternal_surname,email=email).exists():
			data = {'mensaje': 'ya existe ese customer'}
			return JsonResponse(data)	
		else:
			customer.objects.filter(id=id).update(name=name, paternal_surname=paternal_surname,email=email)

			return JsonResponse({"response": "se actualizo con éxito"})

# Borra un registro en customer 
@api_view(['DELETE'])
def delete_customer_api(request):
	rol = verify_jwt(request.headers['Apikey'])
	if rol == "administrator":
		return Response({"error": "solo los super administrator pueden eliminar en customers"})
	elif rol == "super_administrator":
		data=json.loads(request.body)
		name = data['name']
		paternal_surname = data['paternal_surname']
		email = data['email']
		id = data['pk']
		if customer.objects.filter(name=name, paternal_surname=paternal_surname,email=email,id=id).exists():
			registro = customer.objects.get(id=id)
			registro.delete()
			data = {'mensaje': f'El registro con el id {id} se elimino conrrectamente'}
			return JsonResponse(data)	
		else:
			return JsonResponse({"response": "No existe ese registro"})

# Valida el token de autorización
def verify_jwt(jwt_token):
	payload = jwt.decode(jwt_token, 'secret_key', algorithms=['HS256'])
	try:
		payload = jwt.decode(jwt_token, 'secret_key', algorithms=['HS256'])
		name = payload.get('user')
		password = payload.get('password')
		rol = payload.get('rol')

		if administrators.objects.filter(name=name,password=password).exists():
			return rol
	except jwt.exceptions.InvalidTokenError:
		return Response({'error': 'Invalid token'})

# Verificación de logueo
def login_response(request):
	name = request.GET.get('user','')
	password = request.GET.get('password','')

	if administrators.objects.filter(name=name,password=password).exists():
		rol = administrators.objects.get(name=name)
		request.session['login'] = name
		request.session['rol'] = rol.rol

		data = {'mensaje': 'usuario correcto'}
		return JsonResponse(data)	
	else:
		data = {'mensaje': 'usuario o contraseña incorrectos'}
		return JsonResponse(data)

# Renderiza el template del login
def login(request):
	return render(request, 'login.html')

# Desloguea al usuario
def logouts(request):
	logout(request)
	return redirect("login")

# Template que trae los datos de las tablas de customer y payments customer
def menu(request):
	login = request.session.get('login', None)
	rol = request.session.get('rol', None)
	contexto={}
	if login == None:
		return redirect("login")
	if rol == "administrator":
		list_objects , list_objects2 =vistas()
		contexto = {'rol': rol,'object_list':list_objects,'object_list2':list_objects2}
	elif rol == "super_administrator":
		list_objects , list_objects2 =vistas()
		contexto = {'rol': rol,'object_list':list_objects,'object_list2':list_objects2}
	return render(request, 'menu.html',contexto)

# Creación de usuario por medio de la interfaz
def create_customer(request):
	login = request.session.get('login', None)
	rol = request.session.get('rol', None)
	if login == None:
		return redirect("login")
	if rol == "administrator":
		pass
	elif rol == "super_administrator":
		name = request.GET.get('name','')
		paternal_surname = request.GET.get('paternal_surname','')
		email = request.GET.get('email','')
		if customer.objects.filter(name=name, paternal_surname=paternal_surname,email=email).exists():
			data = {'mensaje': 'ya existe ese customer'}
			return JsonResponse(data)	
		else:
			nuevo_registro = customer(name=name, paternal_surname=paternal_surname,email=email)
			nuevo_registro.save()
			payments_customers = payments_customer(amount="10", customer_id=nuevo_registro,product_name="silla",quantity=2)
			payments_customers.save()
			list_objects , list_objects2 =vistas()

			contexto = {'mensaje': 'Se creo customer correctamente','list_objects':list_objects,'list_objects2':list_objects2}
			return JsonResponse(contexto)
	

# Elimina usuario por medio de la interfaz
def eliminar_customer(request):
	login = request.session.get('login', None)
	rol = request.session.get('rol', None)
	if login == None:
		return redirect("login")
	if rol == "administrator":
		return JsonResponse({"error": "solo los super administrator pueden eliminar en customers"})
	elif rol == "super_administrator":
		id = request.GET.get('id','')
		registro = customer.objects.get(id=id)
		registro.delete()
		list_objects , list_objects2 =vistas()
	contexto = {'mensaje': f'se elimino registro con el id {id}','list_objects':list_objects,'list_objects2':list_objects2}
	return JsonResponse(contexto)

# Edita registro por medio de la interfaz
def editar_customer(request):
	login = request.session.get('login', None)
	rol = request.session.get('rol', None)
	if login == None:
		return redirect("login")
	if rol == "administrator":
		return JsonResponse({"error": "solo los super administrator pueden actualizar en customers"})
	elif rol == "super_administrator":
		id = request.GET.get('id','')
		name = request.GET.get('name','')
		paternal_surname = request.GET.get('paternal_surname','')
		email = request.GET.get('email','')
		customer.objects.filter(id=id).update(name=name, paternal_surname=paternal_surname,email=email)
		list_objects , list_objects2 =vistas()
	contexto = {'mensaje': f'Se actualizo correctamente','list_objects':list_objects,'list_objects2':list_objects2}
	return JsonResponse(contexto)

# Consulta datos del registro para actualizar por medio de la modal
def consulta_editar(request):
	login = request.session.get('login', None)
	rol = request.session.get('rol', None)
	if login == None:
		return redirect("login")
	if rol == "administrator":
		id=request.GET.get('id','no')
		object_list1=customer.objects.filter(id=id)
		serialized_objects  = serializers.serialize('json', object_list1)
		json_objects=json.loads(serialized_objects)
		list_objects = []   
		for index in range(len(json_objects)):
			list_id = json_objects[index]['fields']['pk'] = json_objects[index]['pk']
			list_objects.append(json_objects[index]['fields'])
	elif rol == "super_administrator":
		id=request.GET.get('id','no')
		object_list1=customer.objects.filter(id=id)
		serialized_objects  = serializers.serialize('json', object_list1)
		json_objects=json.loads(serialized_objects)
		list_objects = []   
		for index in range(len(json_objects)):
			list_id = json_objects[index]['fields']['pk'] = json_objects[index]['pk']
			list_objects.append(json_objects[index]['fields'])
	return HttpResponse(json.dumps(list_objects), content_type='application/json;charset=utf-8')

# Método que trae los registros de las tablas customer y payments customer
def vistas():

	object_list1 = customer.objects.all()
	serialized_objects  = serializers.serialize('json', object_list1)
	json_objects=json.loads(serialized_objects)
	list_objects = []   
	for index in range(len(json_objects)):
		list_id = json_objects[index]['fields']['pk'] = json_objects[index]['pk']
		list_objects.append(json_objects[index]['fields'])
	object_list2 = payments_customer.objects.all()
	serialized_objects2  = serializers.serialize('json', object_list2)
	json_objects2=json.loads(serialized_objects2)
	list_objects2 = []   
	for index in range(len(json_objects2)):
		list_id = json_objects2[index]['fields']['pk'] = json_objects[index]['pk']
		list_objects2.append(json_objects2[index]['fields'])

	return list_objects, list_objects2