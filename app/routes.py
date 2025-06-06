from flask import Blueprint, render_template
from .services.kenpom_engine import get_kpoy
import json
from pathlib import Path

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
  from app import kenpom_browser

  players_df = get_kpoy(kenpom_browser)
  players_list = players_df.to_dict('records')
  
  team_image_path = Path("app/static/data/team_images.json")
  image_path = Path("app/static/data/player_images.json")
  player_images = json.loads(image_path.read_text())
  team_images = json.loads(team_image_path.read_text())

  return render_template('home.html', players = players_list, image = player_images, team_logo = team_images)


@routes.route('/nba')
def nba():
  return