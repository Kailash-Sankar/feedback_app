// dashboard home page | ksankar 2016

//Trending Unanswered Questions Card
app.controller('trendingQuestions', function($scope, $http, $rootScope, $timeout, jaximus) {

  $scope.trendingItems = [];
  $scope.jaxip=false;
  loadTrending();  

  //indicate when new data is ready
  $scope.newDataAvailable = false;

 //load trending questions
 function loadTrending() { 
  $scope.jaxip=true;   	   
  jaximus.loadDataSet('/trending/questions')
  .success(function(data, status, headers, config) {
   console.log(data);
   $scope.trendingItems = data;
   $scope.jaxip=false;      				
 })
  .error(function(data, status, headers, config) {
    console.log('something went wrong.');
    $scope.jaxip=false;
  });

  jaximus.toastThis('Data loaded');
};

$scope.updateList = function() {
  loadTrending();
};

});

//Trending Answered Questions
app.controller('trendingAnswers', function($scope, $http, $rootScope, $timeout, jaximus) {

  $scope.trendingItems = [];
  $scope.jaxip=false;
  loadTrending();  

  //indicate when new data is ready
  $scope.newDataAvailable = false;

 //load trending questions
 function loadTrending() { 
  $scope.jaxip=true;   	   
  jaximus.loadDataSet('/trending/answers')
  .success(function(data, status, headers, config) {
   console.log(data);      
   $scope.trendingItems = data;
   $scope.jaxip=false;      				
 })
  .error(function(data, status, headers, config) {
    console.log('something went wrong.');
    $scope.jaxip=false;
  });

  jaximus.toastThis('Data loaded.');
};

$scope.updateList = function() {
  loadTrending();
};
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

