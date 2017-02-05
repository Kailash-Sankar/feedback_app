// dashboard home page | ksankar 2016

//Trending Unanswered Questions Card
app.controller('mainFeed', function($scope, $http, $rootScope, $timeout, jaximus) {
  $rootScope.cid = $('input[name="cid"]').val();

  //prep transport data
  $scope.saveTransportForm = function() {
    $scope.data = {
      'cid'         : $rootScope.cid,
      'rating'      : $scope.rated,
      'date'        : $scope.trip_date,
      'type'        : $scope.trip_type,
      'description' : $scope.description
    };
    saveForm();
  }

  //prep the cafeteria data
  $scope.saveCafeteriaForm = function() {
    $scope.data = {
      'cid'         : $rootScope.cid,
      'rating'      : $scope.rated,
      'date'        : $scope.meal_date,
      'loc_id'      : $scope.location,
      'vendor_id'   : $scope.vendor.id
    };
    saveForm();
  }

  // save the main feedback form
  function saveForm() {
    var url = '/cat/' + $rootScope.cid + '/save';
    console.log($scope.data);

    //rating is required while fetching questions
    $rootScope.rating = $scope.data.rating;

    jaximus.saveDataSet(url,$scope.data)
    .success(function(data, status, headers, config) {
      console.log(data);
      if ( data.fid && data.type_id ) {
        $rootScope.fid = data.fid;
        jaximus.toastThis('Trip information saved.');
        $rootScope.$broadcast("loadQ", data);
      }
      else {
        jaximus.toastThis('Save error. Please try agian later.');
      }
    })
    .error(function(data, status, headers, config) {
      jaximus.toastThis('Error. Please try again.');
      console.log('something went wrong.')
    });
  };

  $scope.loadVendors = function(loc){
    var url = '/cat/' + $rootScope.cid + '/loc/' + loc + '/vendors';
    jaximus.loadDataSet(url)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.vendors = data;
      $scope.showQ=true;
    });
  }

  $scope.choose_smiley = function(id) {
    $scope.rated = id;
  };

});

//Trending Answered Questions
app.controller('catQuestions', function($scope, $http, $rootScope, $timeout, $window, jaximus) {

  $scope.questions = [];
  $scope.showQ=false;

  function loadQuestions() {
    var url = '/cat/' + $rootScope.cid + '/questions/' + $rootScope.rating;
    jaximus.loadDataSet(url)
    .success(function(data, status, headers, config) {
      console.log(data);
      $scope.questions = data;
      $scope.showQ=true;
    });
  }

  $rootScope.$on("loadQ", function(data){
    console.log('something is happening',data);
    loadQuestions();
  });

  $scope.saveForm = function() {
    var url = '/cat/' + $rootScope.cid + '/answers/save';
    var data = {
      questions : $scope.questions,
      fid : $rootScope.fid
    }
    console.log('questions',data)

    jaximus.saveDataSet(url,data)
    .success(function(data, status, headers, config) {
      console.log(data);
      jaximus.toastThis('Feedback saved.');
      $window.location.href = '/feed/' + $rootScope.fid + '/view';
    })
    .error(function(data, status, headers, config) {
      jaximus.toastThis('Error. Please try again.');
      console.log('something went wrong.')
    });
  };

});

app.run(function($rootScope) {
  $('input#trip_date,input#meal_date').bootstrapMaterialDatePicker({
    format : 'YYYY-MM-DD hh:mm:ss'
  });
});
