
app.controller('reportMain', function($scope, $http, $rootScope, $timeout, jaximus) {
  $scope.show_summary = 0;

  $scope.loadReport = function() {

    if ( !$scope.cat ) { return; }
    $rootScope.cid = $scope.cat;

    var url = '/report/cat/' + $scope.cat;
    jaximus.loadDataSet(url)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.show_summary = 1;
      $scope.summary = data.summary;
      $scope.category = data.cat;
      console.log(data);
    });
  }

});

app.controller('Answers', function($scope, $rootScope, $timeout, jaximus) {

  //toggle add new form
  $scope.toggleForm = function() {
    $scope.addMode = !$scope.addMode;
  };

  $(window).load(function () {
    $('input[data-required],textarea[data-required]').attr('required', true);
  });

});
