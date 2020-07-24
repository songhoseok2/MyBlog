import React from 'react';
import ReactDOM from 'react-dom';
//import * as serviceWorker from './serviceWorker';

function attachActive(new_active_button, old_active_button)
{
    if (!new_active_button.classList.contains("active"))
    {
        new_active_button.classList.add("active");
        old_active_button.classList.remove("active");
    }
}

window.onload = function () {
    var reveal_button = document.getElementById("reveal_button_id");
    var incognito_button = document.getElementById("incognito_button_id");

    if (reveal_button) reveal_button.onclick = function() { attachActive(reveal_button, incognito_button); }; 
    if (incognito_button) incognito_button.onclick = function() { attachActive(incognito_button, reveal_button); }; 
};



// class BlogPosts extends React.Component
// {
//   render()
//   {
    
//   }
// }

// var blog_posts_div = document.getElementById("blog_posts_id");
// if(blog_posts_div)
// {
//   var posts = {...(blog_posts_div.dataset)};
//   ReactDOM.render(<BlogPosts posts={posts} />, blog_posts_div);
// }





// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
//serviceWorker.unregister();