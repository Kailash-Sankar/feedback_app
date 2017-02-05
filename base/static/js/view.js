
app.controller('Questions', function($scope, $http, $rootScope, $timeout, jaximus) {

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
