import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CourseHomeComponent } from './course-home/course-home.component';
import { HomeComponent } from './home/home.component';
import { GraduateHomeComponent } from './graduate-home/graduate-home.component';
import { ProfileComponent } from './profile/profile.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    children: [
      {
        path: '',
        component: GraduateHomeComponent
      },
      {
        path: 'courses',
        component: CourseHomeComponent
      },
      {
        path: 'profile',
        component: ProfileComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CoursesRoutingModule {}
