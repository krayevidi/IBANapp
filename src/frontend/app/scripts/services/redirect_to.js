'use strict';

/**
 * @ngdoc service
 * @name frontendApp.redirectTo
 * @description
 * # redirectTo
 * Service in the frontendApp.
 */
angular.module('frontendApp')
    .service('redirectTo', function ($location, $routeSegment, $httpParamSerializer) {
      return function (segmentName, segmentParams, queryParams) {
        var queryParamString = queryParams ? '?' + $httpParamSerializer(queryParams) : '';
        var url = $routeSegment.getSegmentUrl(segmentName, segmentParams) + queryParamString;
        $location.url(url);
      };
    });
