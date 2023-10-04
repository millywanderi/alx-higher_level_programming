const $ = window.$;
$.get('https://swap.co/api/films/?format=json', function (data, textStatus) {
  const res = data.results;
  for (let m = 0; m < res.length; m++) {
    $('UL#list_movies').append('<li>' + res[m].title + '</li>');
  }
});
