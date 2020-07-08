import React from 'react';
import ReactDOM from 'react-dom';

class TopNavBar extends React.Component
{
  render()
  {
      return (
        <div>
            <header class="site-header">
                <nav class="navbar navbar-expand-md navbar-dark bg-steel fixed-top">
                <div class="container">
                    <a class="navbar-brand mr-4" href="/">Flask Blog</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarToggle" aria-controls="navbarToggle" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarToggle">
                        <div class="navbar-nav mr-auto">
                        <a class="nav-item nav-link" href="/">Home</a>
                        <a class="nav-item nav-link" href="/about">About</a>
                        </div>
                        <div class="navbar-nav">
                        <a class="nav-item nav-link" href="/login">Login</a>
                        <a class="nav-item nav-link" href="/register">Register</a>
                        </div>
                    </div>
                </div>
                </nav>
            </header>
        </div>
      );
  }
}

class SideNavBar extends React.Component
{
  render()
  {
      return (
        <div>
            <div class="content-section">
            <h3>Our Sidebar</h3>
            <p class='text-muted'>You can put any information here you'd like.
                <ul class="list-group">
                <li class="list-group-item list-group-item-light">Latest Posts</li>
                <li class="list-group-item list-group-item-light">Announcements</li>
                <li class="list-group-item list-group-item-light">Calendars</li>
                <li class="list-group-item list-group-item-light">etc</li>
                </ul>
            </p>
            </div>
        </div>
      );
  }
}


var top_navbar_div = document.getElementById("top_navbar_id");
var side_navbar_div = document.getElementById("side_navbar_id");

if(top_navbar_div) ReactDOM.render(<TopNavBar />, top_navbar_div);
if(side_navbar_div) ReactDOM.render(<SideNavBar />, side_navbar_div);





  