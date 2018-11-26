from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, reverse
from .models import Game, Matchup, Team, Slot, Location
from django.db.models import Q
from datetime import datetime
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    if request.method != "POST":
        return render(request, "all_scores/login.html", {'failure': False})
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        print(user.username)
        login(request, user)
        return HttpResponseRedirect(reverse('index',args=()))
    else:
        return render(request, "all_scores/login.html", context={'failure': True})

def logout_view(request):
    logout(request)
    return render(request, "all_scores/index.html")

def index(request):
    """Initial view"""
    return render(request, "all_scores/index.html", {})

def game(request, game_id):
    """The view for scoring a game"""
    if not request.user.is_authenticated:
        return render(request, 'all_scores/login.html')
    template = "all_scores/game.html"
    alert = False
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404("This game does not exist!")
    matchup = game.matchup
    if request.method == 'POST':
        if 'start' in request.POST:
            game.game_completed = 2 # sets the game to running
        elif request.POST.get('end') or request.POST.get('update'):
            matchup.matchup_team1_score = int(request.POST['team1_score'])
            matchup.matchup_team2_score = int(request.POST['team2_score'])
            matchup.matchup_team1_timeouts = int(request.POST['team1_timeouts'])
            matchup.matchup_team2_timeouts = int(request.POST['team2_timeouts'])
            if request.POST.get('end'):
                game.game_completed = 1 # sets the game to finished
                template = "all_scores/overview.html"
                game.save()
                matchup.save()
                print("HEY")
                return HttpResponseRedirect(reverse('overview', args=()))
            matchup.save()
        game.save()
        alert = True
        return HttpResponseRedirect(reverse('game', args=(game_id,)))

    context = {
        'game' : game,
        'matchup' : matchup,
        'alert' : alert,
    }
    return render(request, template, context)

def overview(request):
    """Overview with filtering options"""
    game_list = Game.objects.all()
    matchup_list = Matchup.objects.all()
    team_list = Team.objects.all()
    slot_list = Slot.objects.all()
    location_list = Location.objects.all()
    location_filtered = False
    status_filtered = False
    selected_location = "All Locations"
    selected_status = "All Matches"
    if request.GET.get('location') and request.GET.get('location') != selected_location:
        loc = request.GET.get('location')
        game_list = game_list.filter(slot__location__location_name=loc)
        selected_location = loc
        location_filtered = True
    if request.GET.get('status') and request.GET.get('status') != selected_status:
        stat = request.GET.get('status')
        if stat == 'Completed':
            game_list = game_list.filter(game_completed=1)
        elif stat == 'Uncompleted':
            game_list = game_list.filter(Q(game_completed=0)| Q(game_completed=2))
        selected_status = stat
        status_filtered = True
    context = {
        'game_list': game_list,
        'matchup_list': matchup_list,
        'team_list': team_list,
        'slot_list': slot_list,
        'location_list': location_list,
        'selected_location': selected_location,
        'selected_status': selected_status,
        'location_filtered': location_filtered,
        'status_filtered': status_filtered,
        'datetime': datetime,
    }
    return render(request, 'all_scores/overview.html', context)
