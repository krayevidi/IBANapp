'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:BankAccountsListCtrl
 * @description
 * # BankAccountsListCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
    .controller('BankAccountsListCtrl', function ($scope, bankAccounts) {
      $scope.bankAccountsList = bankAccounts.getList().$object;
      $scope.deleteBankAccount = function (bankAccount, index) {
        var msg = 'Are you sure you want to delte "{firstName} {lastName}"?'
            .replace('{firstName}', bankAccount.first_name)
            .replace('{lastName}', bankAccount.last_name);
        if (confirm(msg)) {
          bankAccount.remove().then(
              function () {
                $scope.bankAccountsList.splice(index, 1);
              }
          );
        }
      }
    });
