
from .models import Artist
from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse 
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# import models


# Create your views here.


class Home(TemplateView):
    template_name = "home.html"
    

class About(TemplateView):
    template_name = "about.html"

 #adds artist class for mock database data
class Artist:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio


artists = [
  Artist("G Eazy", "https://img.youtube.com/vi/HyanRY9EKj4/0.jpg",
          "erald Earl Gillum (born May 24, 1989), better known by his stage name G-Eazy, is an American rapper."),
  Artist("Hippie Sabotage",
          "https://edm.com/.image/t_share/MTU4NTY4OTg4OTAzNzQ0ODY4/hippiesabotage.jpg", "Hippie Sabotage are an electronic dance music duo from Sacramento, California, consisted of brothers Kevin and Jeff Saurer.[1] They are well known for their remix of Habits (Stay High), which has surpassed 1 billion views on YouTube."),
  Artist("Jez Dior", "https://townsquare.media/site/1096/files/2018/06/Jez_Dior_2017.jpg?w=980&q=75",
          "Jez Dior is a Los Angeles based Hip-Hop artist. His upcoming mixtape Scarlett Sage will mark his first ever solo release. Being the son of 1970s punk rocker Steve Dior  best friend of Sid Vicious and crafter of many Sex Pistols songs, he is no stranger to the music scene."),
  Artist("Shinedown",
          "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/ShinedownThreatToSurvival.jpg/1200px-ShinedownThreatToSurvival.jpg", "Shinedown is an American rock band from Jacksonville, Florida, formed by singer Brent Smith in 2001 after the dissolution of Dreve, his previous band."),
  Artist("Downstait",
          "https://yt3.googleusercontent.com/ytc/AGIKgqPQsmJSidEG1tEHnB2gdbklw7j3At7pVdQMwGn2QQ=s900-c-k-c0x00ffffff-no-rj", "The lead singer of Downstait comments on how 'Kingdom' helped save the band's career."),
  Artist("Logic",
          "https://www.billboard.com/wp-content/uploads/media/logic-bb30-2017-feat-billboard-lssj-1548.jpg?w=942&h=623&crop=1", "Sir Robert Bryson Hall II[a] (born January 22, 1990), known professionally as Logic, is an American rapper, singer, songwriter, and record producer. He has released eight studio albums and received two Grammy Award nominations."),
]
    
class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["artists"] = artists 
        return context

class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_create.html"
    success_url = "/artists/"

class ArtistDetail(DetailView):
    model = Artist
    template_name = "artist_detail.html"

class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_update.html"
    success_url = "/artists/"

class ArtistDelete(DeleteView):
    model = Artist
    template_name = "artist_delete_confirmation.html"
    success_url = "/artists/"