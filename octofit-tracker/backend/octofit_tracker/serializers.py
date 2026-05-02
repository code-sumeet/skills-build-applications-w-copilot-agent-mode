
from rest_framework import serializers
from .models import User, Team, Activity, Leaderboard, Workout

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all(), write_only=True)
    team_detail = TeamSerializer(source='team', read_only=True)
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'team', 'team_detail']

class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    user_detail = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_detail', 'type', 'duration']

class WorkoutSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    user_detail = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'user', 'user_detail']

class LeaderboardSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True)
    user_detail = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_detail', 'points']
