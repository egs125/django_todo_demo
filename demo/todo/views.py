from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Todo

import logging

# get logger instance 
logger = logging.getLogger(__name__)

# def index(request):
#  return HttpResponse("Hello, world")

def index(request):
  todo_list = Todo.objects.order_by("id")[:5]
  template = loader.get_template("todo/index.html")
  context = {'todo_list': todo_list}

  logger.error('.............fetch to-do list')

  logger.debug('This is a debug message')
  logger.info('This is an info message')
  logger.warning('This is a warning message')
  logger.error('This is an error message')
  logger.critical('This is a critical message')

  return HttpResponse(template.render(context, request))