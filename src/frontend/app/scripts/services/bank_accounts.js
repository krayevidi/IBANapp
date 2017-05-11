'use strict';

/**
 * @ngdoc service
 * @name frontendApp.bankAccounts
 * @description
 * # bankAccounts
 * Service in the frontendApp.
 */
angular.module('frontendApp')
  .service('bankAccounts', function (Restangular) {
    return Restangular.service('bank_accounts');
  });
