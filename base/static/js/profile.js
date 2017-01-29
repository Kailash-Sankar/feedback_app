// profile page | ksankar 2016

//load user profile
app.controller('profile', function($scope, $http, $rootScope, $timeout, jaximus) {

	$scope.viewMode = true;
	loadProfile();  

 //load trending questions
 function loadProfile() {    	   
 	jaximus.loadDataSet('/me')
 	.success(function(data, status, headers, config) {
 		console.log(data);
 		$scope.profile = data;

 		//dirty check on mdl fields that we just re-rendered
 		//temp workaround	
 		$timeout(function () { 
            $(".profile-form .mdl-textfield").each( function() {
            	console.log(this);
              $(this).get(0).MaterialTextfield.checkDirty();              
            });
        }, 100, false); 		
 	})
 	.error(function(data, status, headers, config) {
 		console.log('something went wrong.');
 	});

 	jaximus.toastThis('Profile loaded');
 };

 $scope.edit = function() {
 	$scope.viewMode = !$scope.viewMode;
 };

});

//load tags
app.controller('tags', function($scope, $http, $rootScope, $timeout, jaximus) {

   //question data structure
   $scope.tags = [];
   loadTags();

	//load user's tags
	function loadTags() {
		jaximus.loadDataSet('/me/tags')
		.success(function(data, status, headers, config) {
			console.log(data);
			$scope.tags = data;      				
		})
		.error(function(data, status, headers, config) {
			console.log('something went wrong.')
		});
	};

	//tag actions	
	$scope.loadTags = function(query) {
		return $http.get('/tags/'+ query);
	};

    //save user's tags
    $scope.saveTags = function() {
    	console.log('save',$scope.tags);
    	
    	var url = '/me/tags/save'
    	jaximus.saveDataSet(url,$scope.tags)
    	.success(function(data, status, headers, config) {
    		console.log(data);
    		$scope.tags = data;      		
      		jaximus.toastThis('Tags Saved');
		})
		.error(function(data, status, headers, config) {
		  	jaximus.toastThis('Error. Please try again.');
		  	console.log('something went wrong.')
		});	
    };

 });



