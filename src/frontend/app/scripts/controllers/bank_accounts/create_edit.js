'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:BankAccountsCreateEditCtrl
 * @description
 * # BankAccountsCreateEditCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
    .controller('BankAccountsCreateEditCtrl', function ($routeParams, $routeSegment, $uibModal, bankAccounts, redirectTo) {
      var isCreateView = $routeParams.id === 'new';

      function redirectToList() {
        redirectTo('main.bank_accounts_list');
      }

      function openModal(bankAccount) {
        var modalInstance = $uibModal.open({
          templateUrl: 'views/bank_accounts/create_edit_modal.html',
          controller: 'BankAccountsCreateEditModalCtrl',
          size: 'sm',
          resolve: {
            isCreateView: isCreateView,
            bankAccount: bankAccount || {}
          }
        });
        modalInstance.result.then(redirectToList, redirectToList);
      }

      if (isCreateView) {
        openModal();
      } else {
        bankAccounts.one($routeParams.id).get().then(openModal, redirectToList);
      }
    });
