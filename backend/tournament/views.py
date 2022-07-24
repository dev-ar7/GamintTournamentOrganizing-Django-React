from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from .models import *
from .serializers import *


class TeamCreateView(generics.CreateAPIView):

    queryset = Team.objects.all()
    serializer_class = TeamSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request):

        if request.method == 'POST':
            team_name = request.data.get('team_name')
            team_exists = Team.objects.filter(team_name = team_name).exists()
            if team_exists:
                return Response({'message': 'Team Name already exists. Use a different Team Name.'},
                                status=status.HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                {'message': 'Team Registation Successful.'}, 
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, 
                            {'message': 'Request Failed! Invalid Data!'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Method not allowee'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TeamListView(generics.ListAPIView):

    queryset = Team.objects.all()
    serializer_class = TeamSerializers


class TournamentCreateView(generics.CreateAPIView):

    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request):

        if request.method == 'POST':
            name = request.data.get('name')
            name_exist = Tournament.objects.filter(name = name).exists()
            if name_exist:
                return Response({'message': 'Tournament Name already exists. Use a different Team Name.'},
                                status=status.HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                {'message': 'Tournament Hosted Successfully.'}, 
                                status=status.HTTP_201_CREATED)
            return Response(serializer.errors, 
                            {'message': 'Request Failed! Invalid Data!'}, 
                            status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Method not allowee'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class TournamentListView(generics.ListAPIView):

    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializers


class CheckInCreateView(generics.CreateAPIView):

    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request):
        
        if request.method == 'POST':
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                    {'message': 'Checked in Successfully.'}, 
                                    status=status.HTTP_201_CREATED)
            return Response(serializer.errors, 
                                {'message': 'Request Failed! Invalid Data!'}, 
                                status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CheckInListView(generics.ListAPIView):

    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializers


class MatchWinnerCreateView(generics.CreateAPIView):

    queryset = Match.objects.all()
    serializer_class = MatchSerializers
    permission_classes = [IsAdminUser]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request):

        if request.method == 'POST':
            match_round = request.data.get('match_round')
            match_number = request.data.get('match_number')
            match_round_exists = Match.objects.filter(match_round = match_round).exists()
            match_number_exists = Match.objects.filter(match_number = match_number).exists()
            if match_round_exists & match_number_exists:
                return Response({'message': 'Data already exists!'},
                                status=status.HTTP_400_BAD_REQUEST)
            
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                    {'message': 'Match data saved Successfully.'}, 
                                    status=status.HTTP_201_CREATED)
            return Response(serializer.errors, 
                                {'message': 'Request Failed! Invalid Data!'}, 
                                status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class MatchWinnerListView(generics.ListAPIView):

    queryset = Match.objects.all()
    serializer_class = MatchSerializers


class CommentCreateView(generics.CreateAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSeializers
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def post(self, request):

        if request.method == 'POST':
            author = request.data.get('author')
            author_exists = Comment.objects.filter(author = author).exists()
            message = request.data.get('message')
            message_exists = Comment.objects.filter(message = message).exists()
            if author_exists & message_exists:
                return Response({'message': 'You have already messaged the same thing!'},
                                status=status.HTTP_400_BAD_REQUEST)

            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,
                                    {'message': 'Commented Successfully.'}, 
                                    status=status.HTTP_201_CREATED)
            return Response(serializer.errors, 
                                {'message': 'Request Failed! Invalid Data!'}, 
                                status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class CommentListView(generics.ListAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSeializers