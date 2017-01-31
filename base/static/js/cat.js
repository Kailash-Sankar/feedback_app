// dashboard home page | ksankar 2016

//Trending Unanswered Questions Card
app.controller('mainFeed', function($scope, $http, $rootScope, $timeout, jaximus) {
  $rootScope.cid = $('input[name="cid"]').val();

  $scope.saveForm = function() {
    var url = '/cat/' + $rootScope.cid + '/save';

    $scope.data = {
      'cid'         : $rootScope.cid,
      'rating'      : $scope.rated,
      'date'        : $scope.trip_date,
      'type'        : $scope.trip_type,
      'description' : $scope.description
    };

    jaximus.saveDataSet(url,$scope.data)
    .success(function(data, status, headers, config) {
      console.log(data);
      jaximus.toastThis('Trip information saved.');
      $rootScope.$broadcast("loadQ", {});
    })
    .error(function(data, status, headers, config) {
      jaximus.toastThis('Error. Please try again.');
      console.log('something went wrong.')
    });
  };

  $scope.choose_smiley = function(id) {
    $scope.rated = id;
  };

});

//Trending Answered Questions
app.controller('catQuestions', function($scope, $http, $rootScope, $timeout, jaximus) {

  $scope.questions = [];
  $scope.showQ=false;

  function loadQuestions() {
   var url = '/cat/' + $rootScope.cid + '/questions';
   jaximus.loadDataSet(url)
   .success(function(data, status, headers, config) {
      console.log(data);
      $scope.questions = data;
      $scope.showQ=true;
  });
  }

  $rootScope.$on("loadQ", function(){
      console.log('something is happening');
      loadQuestions();
  });

});




//My Questions
app.controller('myQuestions', function($scope, $http, $rootScope, $timeout, jaximus) {

  $scope.trendingItems = [];
  $scope.jaxip=false;
  loadTrending();

  //indicate when new data is ready
  $scope.newDataAvailable = false;

 //load trending questions
 function loadTrending() {
  $scope.jaxip=true;
  jaximus.loadDataSet('/trending/my')
  .success(function(data, status, headers, config) {
    console.log(data);
    $scope.jaxip=false;
    $scope.trendingItems = data;
  })
  .error(function(data, status, headers, config) {
    console.log('something went wrong.');
    $scope.jaxip=false;
  });

  jaximus.toastThis('Data loaded.');
}

$scope.updateList = function() {
  loadTrending();
};

});

app.run(function($rootScope) {
  $('input#trip_date').bootstrapMaterialDatePicker({
    format : 'YYYY-MM-DD hh:mm:ss'
  });
});
