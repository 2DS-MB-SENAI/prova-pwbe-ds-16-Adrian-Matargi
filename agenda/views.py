from django.shortcuts import render, get_object_or_404
from .models import Servico, Agendamento
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ServicoSerializer, AgendamentoSerializer

@api_view(['GET', 'POST'])
def servicos(request):
    if request.method == 'GET':
        servicos = Servico.objects.all()
        if not servicos.exists():
            return Response(
                {"mensagem": "Nenhum serviço encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def servico_detalhado(request, id):
    servico = get_object_or_404(Servico, pk=id)

    if request.method == 'GET':
        serializer = ServicoSerializer(servico)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ServicoSerializer(servico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET', 'POST'])
def agendamentos(request):
    if request.method == 'GET':
        agendamentos = Agendamento.objects.all()
        if not agendamentos.exists():
            return Response(
                {"mensagem": "Nenhum agendamento encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = AgendamentoSerializer(agendamentos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def agendamento_detalhado(request, id):
    agendamento = get_object_or_404(Agendamento, pk=id)

    if request.method == 'GET':
        serializer = AgendamentoSerializer(agendamento)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AgendamentoSerializer(agendamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
