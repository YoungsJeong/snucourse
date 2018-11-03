import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NotFoundComponent } from './not-found.component';
import { AuthGuard } from './auth.guard';

const routes: Routes = [
  {
    path: 'intro',
    loadChildren: 'app/intro/intro.module#IntroModule',
    canLoad: [AuthGuard]
  },
  {
    path: 'signup',
    loadChildren: 'app/signup/signup.module#SignupModule',
    canLoad: [AuthGuard]
  },
  {
    path: '',
    loadChildren: 'app/courses/courses.module#CoursesModule',
    canLoad: [AuthGuard]
  },
  {
    path: '**',
    component: NotFoundComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
