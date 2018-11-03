import { NgModule } from '@angular/core';
import { SharedModule } from '../shared/shared.module';

import { CoursesRoutingModule } from './courses-routing.module';
import { CourseDetailComponent } from './course-detail/course-detail.component';
import { CourseListComponent } from './course-list/course-list.component';
import { CourseHomeComponent } from './course-home/course-home.component';
import { CourseSearchComponent } from './course-search/course-search.component';
import { GraduateHomeComponent } from './graduate-home/graduate-home.component';
import { HomeComponent } from './home/home.component';
import { NavbarComponent } from './navbar/navbar.component';
import { ProfileComponent } from './profile/profile.component';
import { ProfileUserinfoComponent } from './profile-userinfo/profile-userinfo.component';
import { ProfileUserhistoryComponent } from './profile-userhistory/profile-userhistory.component';

@NgModule({
  imports: [SharedModule, CoursesRoutingModule],
  declarations: [
    CourseDetailComponent,
    CourseListComponent,
    CourseHomeComponent,
    CourseSearchComponent,
    GraduateHomeComponent,
    HomeComponent,
    NavbarComponent,
    ProfileComponent,
    ProfileUserinfoComponent,
    ProfileUserhistoryComponent
  ]
})
export class CoursesModule {}
