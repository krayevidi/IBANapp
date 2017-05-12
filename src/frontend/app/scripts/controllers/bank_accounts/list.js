'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:BankAccountsListCtrl
 * @description
 * # BankAccountsListCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
    .controller('BankAccountsListCtrl', function ($scope, $rootScope, bankAccounts, redirectTo) {
      function getBankAccountsList() {
        $scope.bankAccountsList = bankAccounts.getList().$object;
      }

      getBankAccountsList();

      $scope.redirectToBankAccountEdit = function (id) {
        redirectTo('main.bank_accounts_list.create_edit', {id: id});
      };

      $scope.deleteBankAccount = function (event, bankAccount, index) {
        event.stopPropagation();
        var msg = 'Are you sure you want to delete "{firstName} {lastName}"?'
            .replace('{firstName}', bankAccount.first_name)
            .replace('{lastName}', bankAccount.last_name);
        if (confirm(msg)) {
          bankAccount.remove().then(
              function () {
                $scope.bankAccountsList.splice(index, 1);
              }
          );
        }
      };

      $scope.$on('bank-account-list:update', getBankAccountsList);
    });
