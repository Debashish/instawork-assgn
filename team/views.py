# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import QueryDict, JsonResponse
from team.models import Team
import string
import random
import json

# Create your views here.

def checkAllFields(req_body):

	val = req_body['member'].values()

	if len(val) == 5:
		return True
	else:
		return False

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def getAllMembers(request):

	results = Team.objects.all()
	lst = []
	for result in results:
		temp_dct = {}
		temp_dct['member_id'] = result.memberid
		temp_dct['first_name'] = result.firstname
		temp_dct['last_name'] = result.lastname
		temp_dct['phone_no'] = result.phonenumber
		temp_dct['email'] = result.email
		temp_dct['role'] = result.role
		lst.append(temp_dct)

	result_dct = {"members":lst}
	return JsonResponse(result_dct)

def addTeamMember(request):

	req_body = json.loads(request.body)
	print req_body

	bool_val = checkAllFields(req_body)

	if bool_val == False:

		error = {"Error": "One more fields are missing"}

		return jsonify(error)

	else:

		member_id = id_generator()
		first_name = req_body['member']['first_name']
		last_name = req_body['member']['last_name']
		email = req_body['member']['email']
		phone_no = req_body['member']['phone_no']
		role = req_body['member']['role']

		try:
			Team.objects.create(memberid=member_id, firstname=first_name, lastname=last_name, phonenumber=phone_no, email=email, role=role)
			result_dct = {"member": {"member_id":member_id, "first_name":first_name, "last_name":last_name, "phone_no": phone_no, "email": email, "role": role}}
			return JsonResponse(result_dct)
		except:
			error = {"Error": "Internal server error"}
			return JsonResponse(error)

def redactTeamMember(request, member_id):

	if request.method == "PUT":
		req_body = json.loads(request.body)
		new_properties = req_body['member']

		if len(new_properties.values()) == 0:

			error = {"Error": "Fields cannot be empty"}

			return JsonResponse(error)

		else:
			try:
				member_obj = Team.objects.get(memberid=member_id)
			except:
				return JsonResponse({"Error": "Team member doesnot exist"})

			try:
				for key, value in new_properties.iteritems():
					if "phone_no" in key:
						member_obj.phonenumber = value
					if "first_name" in key:
						member_obj.firstname = value
					if "last_name" in key:
						member_obj.lastname = value
					if "email" in key:
						member_obj.email = value
					if "role" in key:
						member_obj.role = value
				member_obj.save()

				member = {"member_id":member_id}

				for key, val in new_properties.iteritems():
					member[key] = val
				result_dct = {"member": member}
				return JsonResponse(result_dct)
			except:
				error = {"Error": "The team member does not exist"}
				return JsonResponse(error)

	if request.method == "DELETE":
		try:
			member_obj = Team.objects.get(memberid=member_id)
			member_obj.delete()
			result_dct = {"member": {}}
			return JsonResponse(result_dct)
		except:
			error = {"Error": "Internal server error"}
			return JsonResponse(error)
	
