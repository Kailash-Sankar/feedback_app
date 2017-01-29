
app.controller('ask', function($scope,$http,$rootScope,jaximus,$window) {
	   
    //question data structure
	$scope.q = {
		summary : '',
		description : '',
		tags : [],
	};
	
	//tag actions	
    $scope.loadTags = function(query) {
        return $http.get('/tags/'+ query);
     };

    $scope.saveQuestion = function() {
    	console.log('save',$scope.q);
    	
    	var url = '/question/save'
    	jaximus.saveDataSet(url,$scope.q)
    	.success(function(data, status, headers, config) {
    		console.log(data);
      		//$rootScope.content = data;      				
      		//$('#content').html(data);

      		//redirect to question page
      		jaximus.toastThis('Question Saved.');
      		$window.location.href = '/question/' + data.qid;
      		
		})
		.error(function(data, status, headers, config) {
		  	jaximus.toastThis('Error. Please try again.');
		  	console.log('something went wrong.')
		});
    };

});

//onload set required fields
//workaround for mdl behavior
$(window).load(function () {
	$('input[data-required],textarea[data-required]').attr('required', true);
});

