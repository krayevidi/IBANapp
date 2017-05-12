'use strict';

/**
 * @ngdoc directive
 * @name frontendApp.directive:watchBackendErrors
 * @description
 * Used on form element
 */
angular.module('frontendApp')
    .directive('watchBackendErrors', function () {
      return {
        require: 'form',
        restrict: 'A',
        link: function (scope, element, attr, form) {
          function watchFn() {
            return form.backendErrors
          }

          function watchCallback(newVal) {
            if (newVal) {
              angular.forEach(newVal, function (value, fieldName) {
                if (form[fieldName]) {
                  form[fieldName].$setValidity('backend', false);
                  form[fieldName].backendErrors = value;
                }
              })
            }
          }

          scope.$watchCollection(watchFn, watchCallback);
        }
      }
    });
