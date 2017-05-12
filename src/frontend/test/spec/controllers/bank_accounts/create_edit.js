'use strict';

describe('Controller: BankAccountsCreateEditCtrl', function () {

  // load the controller's module
  beforeEach(module('frontendApp'));

  var BankAccountsCreateEditCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    BankAccountsCreateEditCtrl = $controller('BankAccountsCreateEditCtrl', {
      $scope: scope
      // place here mocked dependencies
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(BankAccountsCreateEditCtrl.awesomeThings.length).toBe(3);
  });
});
