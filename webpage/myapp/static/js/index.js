// Scripts

document.addEventListener('play', function(e){
  var songs = document.getElementsByTagName('audio');
  for(var i = 0, len = songs.length; i < len;i++){
      if(songs[i] != e.target){
          songs[i].pause();
      }
  }
}, true);