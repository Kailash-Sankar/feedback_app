
app.controller('Questions', function($scope, $http, $rootScope, $timeout, jaximus) {
   $rootScope.qid = $('input[name="qid"]').val(); //default to zero


    loadQuestion();

    //load question for a qid
    function loadQuestion() {
      var url = '/q/' + $rootScope.qid;
      jaximus.loadDataSet(url)
      .success(function(data, status, headers, config) {
        console.log(data);
        $scope.q = data;
      })
      .error(function(data, status, headers, config) {
        console.log('something went wrong.')
      });

      jaximus.toastThis('Data loaded.');
    };

});


app.controller('Answers', function($scope, $rootScope, $timeout, jaximus) {

  console.log('hitting this');

  //defaults
  $scope.answers = [];
  $scope.noa = 0;
  $scope.page = 1;
  $scope.addMode = false;
  $scope.new = {};

  $scope.jaxip=false;
  loadAnswers();

  //indicate when new data is ready
  $scope.newDataAvailable = false;

  //load answers for a qid
  function loadAnswers() {
    $scope.jaxip=true;
    var url = $rootScope.qid + '/answers/' + $scope.page;
    jaximus.loadDataSet(url)
    .success(function(data, status, headers, config) {
    	console.log(data);
     $scope.jaxip=false;
     $scope.answers = data;
     $scope.noa =  Object.keys($scope.answers).length;
   })
    .error(function(data, status, headers, config) {
      $scope.jaxip=false;
      console.log('something went wrong.')
    });

    jaximus.toastThis('Data loaded.');
  }

  $scope.updateList = function() {
    loadAnswers();
  };

  //toggle add new form
  $scope.toggleForm = function() {
    $scope.addMode = !$scope.addMode;
  };

  $scope.saveAnswer = function() {
    console.log('save',$scope.new);

    var url = '/question/' + $rootScope.qid + '/answer/save';
    $scope.new.qid = $rootScope.qid;
    jaximus.saveDataSet(url,$scope.new)
    .success(function(data, status, headers, config) {
      console.log(data);

        //add the new answer
        $scope.answers[data.aid] = data;

        //reset add form
        $scope.addMode = false;
        $scope.new = {};
        $scope.noa =  Object.keys($scope.answers).length;
        jaximus.toastThis('Answer Saved.');

      })
    .error(function(data, status, headers, config) {
      jaximus.toastThis('Error. Please try again.');
      console.log('something went wrong.')
    });
  };

  $(window).load(function () {
    $('input[data-required],textarea[data-required]').attr('required', true);
  });


});
