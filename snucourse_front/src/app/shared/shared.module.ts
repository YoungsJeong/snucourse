import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoadingComponent } from './loading/loading.component';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import {
  NgbModule,
  NgbTypeaheadModule,
  NgbDropdownModule,
  NgbModalModule
} from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    FormsModule,
    NgbModule,
    NgbTypeaheadModule,
    NgbDropdownModule,
    NgbModalModule
  ],
  declarations: [LoadingComponent],
  exports: [
    CommonModule,
    LoadingComponent,
    ReactiveFormsModule,
    FormsModule,
    NgbModule,
    NgbTypeaheadModule,
    NgbDropdownModule,
    NgbModalModule
  ]
})
export class SharedModule {}
