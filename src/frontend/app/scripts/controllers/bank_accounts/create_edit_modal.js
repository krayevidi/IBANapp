'use strict';

/**
 * @ngdoc function
 * @name frontendApp.controller:BankAccountsCreateEditModalCtrl
 * @description
 * # BankAccountsCreateEditModalCtrl
 * Controller of the frontendApp
 */
angular.module('frontendApp')
    .controller('BankAccountsCreateEditModalCtrl', function ($rootScope, $scope, $uibModalInstance, bankAccounts, isCreateView, bankAccount) {
      $scope.submitInProgress = false;
      $scope.isCreateView = isCreateView;
      $scope.bankAccount = bankAccount;
      $scope.forms = {
        bankAccountForm: {}
      };
      $scope.save = function (form, instance) {
        $scope.submitInProgress = true;
        function successCallback() {
          $rootScope.$broadcast('bank-account-list:update');
          $uibModalInstance.close();
          $scope.submitInProgress = false;
        }

        function errorCallback(response) {
          form.backendErrors = response.data;
          $scope.submitInProgress = false;
        }

        if (isCreateView) {
          bankAccounts.post(instance).then(successCallback, errorCallback)
        } else {
          instance.save().then(successCallback, errorCallback)
        }
      };
      $scope.cancel = function () {
        $uibModalInstance.dismiss();
      };
    });
