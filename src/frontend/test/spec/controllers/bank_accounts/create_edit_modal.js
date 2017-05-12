'use strict';

describe('Controller: BankAccountsCreateEditModalCtrl', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var BankAccountsCreateEditModalCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    BankAccountsCreateEditModalCtrl = $controller('BankAccountsCreateEditModalCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(BankAccountsCreateEditModalCtrl.awesomeThings.length).toBe(3);
  });
});
