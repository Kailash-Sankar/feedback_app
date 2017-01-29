// Angular base app | ksankar 2016

var app = angular.module('dashboard', ['ngTagsInput']);

//ajax service
app.factory('jaximus', function ($http, $rootScope, $timeout) {
  return {

      //toast status messages
      toastThis : function(msg) {
        $rootScope.toast = {
         msg: msg,
         show: true
       };
       $timeout(function() {
         $rootScope.toast.show = false;
       },2000);
      },

      //loads a chunk of data
      loadDataSet : function(url) {
        return $http.get(url);   
      },

      //post actions
      likePost : function(type,id,like,myLike) {
        var req = {
          method: 'POST',
          url: '/' + type + '/' + id + '/like',          
          data: { 
            'like' : like,
            'myLike' : myLike
            //'csrfmiddlewaretoken' : $('input[name="csrfmiddlewaretoken"]').val()
          }
        };
        return $http(req);
      },

      //post data
      saveDataSet : function(url,data) {
        var req = {
          method: 'POST',
          url: url,
          data: data
        };
        return $http(req);  
      } 
  };
});


// Material design lite isn't fine with dynamic reconstruction of pages.
// The mutation observer makes sure that all new fileds are registered with MDL
app.run(function($rootScope) {
  var mdlUpgradeDom = false;
  setInterval(function() {
    if (mdlUpgradeDom) {
      componentHandler.upgradeDom();
      mdlUpgradeDom = false;
    }
  }, 200);

  var observer = new MutationObserver(function() {
    mdlUpgradeDom = true;
  });
  observer.observe(document.body, {
    childList: true,
    subtree: true
  });
  /* support <= IE 10
  angular.element(document).bind('DOMNodeInserted', function(e) {
      mdlUpgradeDom = true;
  });
  */
  
  // globals
  $rootScope.bgClr = ['x0','x1','x2','x3','x4','x5'];
  
});

///csrf token for ajax calls
app.config(['$httpProvider', function($httpProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

//sorting for the complex data
app.filter('orderObjectBy', function(){
 return function(input, attribute) {
    if (!angular.isObject(input)) return input;

    var array = [];
    for(var objectKey in input) {
        array.push(input[objectKey]);
    }

    array.sort(function(a, b){
        a = parseInt(a[attribute]);
        b = parseInt(b[attribute]);
        return a - b;
    });
    return array;
 }
});

//reversing array sort
app.filter('reverse', function() {
  return function(items) {
    return items.slice().reverse();
  };
});

//attach global utility routines
app.run(function($rootScope,$window) {
        
        //redirect to question page
        $rootScope.redirQ = function(qid) {
            console.log('redirection to',qid);
            $window.location.href = '/question/' + qid;
        };

        //redirect to question with 'focus' on answer

});

//global redir for the non-anchor tags
$('.redir-click').on('click',function(){
  var url = $(this).attr('data-href');
  console.log('redirecting',url);
  window.location.href = url;
})

/* dirty bit check on updated mdl form elements
app.directive('mdlDirtyCheck', ['$timeout', function ($timeout) {
  return {
    link: function ($scope, element, attrs) {
      $scope.$on('dataloaded', function () {
        console.log('data directive exec');
        $timeout(function () { 
            $("form .mdl-textfield").each( function() {
              $(this).get(0).MaterialTextfield.checkDirty();              
            });
        }, 100, false);
      })
    }
  };
}]);

app.directive('eatClick', function() {
    return function(scope, element, attrs) {
        $(element).click(function(event) {
            event.preventDefault();
        });
    };
});
*/